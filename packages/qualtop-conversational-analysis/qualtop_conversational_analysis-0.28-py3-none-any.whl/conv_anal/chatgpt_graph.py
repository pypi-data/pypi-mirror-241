import os
import openai
import networkx as nx
import matplotlib.pyplot as plt

from langchain.graphs.networkx_graph import KnowledgeTriple
from langchain.llms import OpenAI
from langchain.indexes import GraphIndexCreator
from langchain.chains import GraphQAChain
from langchain.prompts import PromptTemplate

from conv_anal.gentera import generate_db_summaries


def show_graph(kg):
    # Create directed graph
    G = nx.DiGraph()
    for node1, relation, node2 in kg:
        G.add_edge(node1, node2, label=relation)
    
    # Plot the graph
    plt.figure(figsize=(25, 25), dpi=300)
    pos = nx.spring_layout(G, k=2, iterations=50, seed=0)
    
    nx.draw_networkx_nodes(G, pos, node_size=5000)
    nx.draw_networkx_edges(G, pos, edge_color='gray', edgelist=G.edges(), width=2)
    nx.draw_networkx_labels(G, pos, font_size=12)
    edge_labels = nx.get_edge_attributes(G, 'label')
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels, font_size=12)
    
    # Display the plot
    plt.axis('off')
    plt.show()

def main():
    # Setup openai
    openai_key=os.environ["OPENAI_API_KEY"]
    openai.api_key = openai_key
    
    # Get information
    _, db_triplets = generate_db_summaries()

    # Start graph
    index_creator = GraphIndexCreator(llm=OpenAI(temperature=0))
    graph = index_creator.from_text("")
    
    for (v1, rel, v2) in db_triplets:
        graph.add_triple(KnowledgeTriple(v1, rel, v2))

    question = "Quien necesita mejorar sus skills de sap"
    chain = GraphQAChain.from_llm(OpenAI(temperature=0), graph=graph, verbose=True)
    chain.run(question)

if __name__ == "__main__":
    main()
