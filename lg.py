from typing import TypedDict
from langgraph.graph import StateGraph, START, END

class MyState(TypedDict):
    input_text: str
    processed: str | None

graph = StateGraph(MyState)


def node_input(state: MyState) -> dict:
    text = state["input_text"]
    processed = text.upper()  # simple processing
    return {"processed": processed}

def node_final(state: MyState) -> dict:
    processed = state["processed"]
    return {"result": f"Final: {processed}"}

graph.add_node("input_node", node_input)
graph.add_node("final_node", node_final)

graph.add_edge(START, "input_node")
graph.add_edge("input_node", "final_node")
graph.add_edge("final_node", END)

initial = MyState(input_text="hello world", processed=None)
final_state = graph.invoke(initial)

print(final_state)
