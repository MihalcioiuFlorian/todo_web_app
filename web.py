import streamlit as st
# streamlit library for creating web apps - popular now bc it's easier
# to create web apss text boxes, buttons, etc
# streamlit run to_do_app/web.py  - command for render web app
import functions

todos = functions.get_todos()


def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)

st.title("My Todo App")
st.subheader("This is my todo app.")
st.write("This app is to increase your productivity")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)  #write the updated todos
        del st.session_state[todo]
        st.experimental_rerun()   #update live after a new action

st.text_input(label="Enter a to-do:", placeholder="Add new todo...",
              on_change=add_todo, key='new_todo')
# the app is hosted in our computer now
# you need a hosting service to get the app online

#st.session_state  # shows live the data added and edited in the web app,
# it will help when develping the app, and it must be deleted before publishing the app
# this is a very specific object of streamlit
# will contain pairs of data that user enters
