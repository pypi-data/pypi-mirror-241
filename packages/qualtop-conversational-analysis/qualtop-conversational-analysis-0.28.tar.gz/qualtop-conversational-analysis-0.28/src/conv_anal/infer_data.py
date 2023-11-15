# -*- coding:utf-8 -*-
import os
import numpy as np
import pandas as pd
import csv_schema_inference

import ppscore as pps

from csv_schema_inference.csv_schema_inference import CsvSchemaInference

from conv_anal.time_series import add_month_day_year_cols

def load_csv(csv_path, header=True, sep=","):
    
    # Infer csv schema
    conditions = {"INTEGER" : "FLOAT"}
    csv_infer = CsvSchemaInference(acc=0.8, 
                                   header=header,
                                   sep=sep,
                                   conditions=conditions)
    
    # Prepare variables
    if header == True:
        header = 0
    
    try:
        inferred_schema = csv_infer.run_inference(csv_path)
    except:
        # Assume everything is textual or categorical
        inferred_schema = {}
        df = pd.read_csv(csv_path, sep=sep, header=header)
        i = 0
        for col in df.columns:
            col_type = {'name':col}
            try:
                unique_values = df[col].dropna().unique().to_list()
                if len(unique_values) > 20:
                    # String
                    col_type['type'] = 'STRING'
                else:
                    # categorical
                    col_type['type'] = 'CATEGORY'
            except:
                col_type['type'] = 'STRING'
            inferred_schema[i] = col_type
            i += 1
        return df

    # Force pandas to load dtypes
    dtypes = {}
    parse_dates = []
    for i in range(len(inferred_schema)):
        data_type = inferred_schema[i]
        data_type['name'] = data_type['name'].\
                encode('latin-1').decode("utf8")
        if data_type["type"] == "INTEGER":
            dtypes[data_type['name']] = np.int_
        elif data_type["type"] == "FLOAT":
            dtypes[data_type['name']] = np.float_
        elif data_type["type"] == "STRING":
            dtypes[data_type['name']] = np.str_
        elif data_type["type"] == "BOOLEAN":
            dtypes[data_type['name']] = np.bool_
        elif data_type["type"] == "DATE":
            parse_dates.append(data_type['name'])
        elif data_type["type"] == "TIMESTAMP":
            dtypes[data_type['name']] = pd.Timestamp
        else:
            raise ValueError(f"Couldn't infer schema for {data_type['name']}")
    
    df=pd.read_csv(csv_path, sep=sep, dtype=dtypes, header=header, parse_dates=parse_dates)
    return df

def get_unique_values(df, col):
    return df[col].dropna().unique().tolist()


def get_primary_key_candidates(dataframes):
    candidates = set({})
    for df in dataframes:
        new_candidates = set(df.columns)
        candidates = candidates.intersection(new_candidates)
        if len(candidates) == 0:
            candidates = new_candidates
    # Only select variables with unique integers
    final_candidates = []
    for candidate in candidates:
        if dataframes[0][candidate].dtype == np.int_ :
            total_values = len(get_unique_values(dataframes[0], candidate))
            if total_values == dataframes[0].shape[0]:
                final_candidates.append(candidate)
    return final_candidates

def get_id_candidates(dataframe):
    cols = list(dataframe.columns)
    id_candidates = []
    for col in cols:
        total_values = len(get_unique_values(dataframe, col))
        if total_values == dataframe.shape[0]:
            id_candidates.append(col)
    return id_candidates

def get_constant_variables(dataframe):
    cols = list(dataframe.columns)
    constant_variables = []
    for col in cols:
        total_values = len(get_unique_values(dataframe, col))
        if total_values == 1:
            constant_variables.append(col)
    return constant_variables

def merge_dataframes(dataframes):
    assert len(dataframes) > 1
    # Get possible primary keys
    primary_key_candidates = get_primary_key_candidates(dataframes)
    if len(primary_key_candidates) > 0:
        # Take any
        primary_key = primary_key_candidates.pop()
    else:
        raise ValueError("Couldn't find primary key candidates")

    # Merge based on the selected key 
    last_df = dataframes[0]
    for df in dataframes[1:]:
        last_df = last_df.merge(df, how="inner", on=primary_key)

    return last_df

def get_schema(dataframe):
    cols = list(dataframe.columns)
    types = []
    for col in cols:
        types.append(str(dataframe[col].dtype))
    return [k for k in zip(cols, types)]

def calculate_prediction_power(df, pred_var = ["x", "y", "case", "model_score", "ppscore"]):
    pred_scores = []
    var_types = get_schema(df)
    for col, c_type in var_types:
        if "datetime" not in c_type:
            pred = pps.predictors(df, col)
            pred_scores.append(pred[pred_var].copy())
    return pred_scores

def describe_dataset(df, name="df", category_cutoff=20, basic_measures=["mean", "max", "min", "std"]):
    message = f"El dataframe 'df', cargado del archivo {name}, tiene las siguientes columnas:\n"
    message += f"\"\"\"\n"
    var_types = get_schema(df)
    numeric_types = []
    unique_values = {}
    categorical_types = []
    # TYPES
    for var, vtype in var_types:
        message += f"\t'{var}' de tipo {vtype}\n"
        if "date" not in vtype and "object" not in vtype:
            numeric_types.append(var)
        else:
            unique_values[var] = get_unique_values(df, var)
            if len(unique_values[var]) <= category_cutoff:
                categorical_types.append(var)
    message += "\n"
    
    # POSSIBLE KEYS
    id_candidates = get_id_candidates(df)
    numeric_types = list(set(numeric_types).difference(set(id_candidates)))
    if len(id_candidates) > 0:
        message += f"\tEstas columnas son posibles llaves primarias: {str(id_candidates)[1:-1]}\n"
    
    # CONSTANT VALUES
    constant_variables = get_constant_variables(df)
    numeric_types = list(set(numeric_types).difference(set(constant_variables)))
    if len(constant_variables) > 0:
        message += f"\tEstas columnas tienen valores constantes: {str(constant_variables)[1:-1]}\n"
        for col in constant_variables:
            message += f"\t\t'{col}' tiene como valor: '{df[col][0]}'\n"
    

    message += "\n"
    # BASIC STATISTICS
    desc_df = df.describe()
    for n_type in numeric_types:
        for measure in basic_measures:
            message += f"\t'{n_type}' tiene un valor {measure} de {desc_df[n_type][measure]}\n"
    
    message += "\n"
    
    # CATEGORICAL VALUES
    categorical_types = list(set(categorical_types).difference(set(constant_variables)))
    if len(categorical_types) > 0:
        # Count
        for var in categorical_types:
            for value in unique_values[var]:
                var_count = df[var][df[var]==value].count()
                message += f"\tHay {var_count} registros que tienen '{value}' en la variable '{var}'.\n"

    message += "\n"
    message += f"\tEl dataframe tiene {df.shape[0]} registros.\n"
    message += "\"\"\"\n"
    
    return message

def analyse_dataset(csv_path):
    fname = os.path.basename(csv_path)
    if fname.endswith(".csv"):
        df = load_csv(csv_path)
        var_type = get_schema(df)
        for col, c_type in var_type:
            if "datetime" in c_type:
                add_month_day_year_cols(df, col)
        description = describe_dataset(df, fname)
    else:
        raise ValueError("Not a csv file")
    return df, description
