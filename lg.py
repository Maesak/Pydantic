from typing import TypedDict
from langgraph.graph import StateGraph, START, END

# 1. Define your State schema using TypedDict
class MyState(TypedDict):
    input_text: str
    processed: str | None

# 2. Create a StateGraph with that state
graph = StateGraph(MyState)

# 3. Define nodes (functions) that take the state and return a partial update

def node_input(state: MyState) -> dict:
    # This node might read `input_text` and do something
    text = state["input_text"]
    processed = text.upper()  # simple processing
    return {"processed": processed}

def node_final(state: MyState) -> dict:
    # This node reads processed value and maybe do final step
    processed = state["processed"]
    return {"result": f"Final: {processed}"}

# 4. Add nodes to the graph and link them with edges
graph.add_node("input_node", node_input)
graph.add_node("final_node", node_final)

# You need to set which node is START and which transitions to which
graph.add_edge(START, "input_node")
graph.add_edge("input_node", "final_node")
graph.add_edge("final_node", END)

# 5. Invoke the graph with initial state
initial = MyState(input_text="hello world", processed=None)
final_state = graph.invoke(initial)

print(final_state)
