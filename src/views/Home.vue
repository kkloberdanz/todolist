<template>
    <div id="app">
        <AddTodo @add-todo="addTodo" />
        <Todos v-bind:todos="todos" @del-todo="deleteTodo" />
    </div>
</template>

<script>
import Todos from "../components/Todos";
import AddTodo from "../components/AddTodo";
import axios from "axios";

export default {
    name: "Home",
    components: {
        Todos,
        AddTodo,
    },

    data() {
        return {
            todos: [],
        };
    },

    methods: {
        deleteTodo(id) {
            this.todos = this.todos.filter((x) => x.id !== id);
            axios
                .delete(`http://127.0.0.1:5000/todos/${id}`)
                /* eslint-disable no-unused-vars */
                .then((res) => {})
                /* eslint-enable no-unused-vars */
                .catch((err) => console.log(err));
        },

        addTodo(newTodo) {
            const { title, completed } = newTodo;
            axios
                .post("http://127.0.0.1:5000/todos", {
                    title,
                    completed,
                })
                .then((res) => (this.todos = res.data))
                .catch((err) => console.log(err));
        },
    },

    created() {
        axios
            .get("http://127.0.0.1:5000/todos")
            .then((res) => {
                this.todos = res.data;
                console.log(res.data);
            })
            .catch((err) => console.log(err));
    },
};
</script>

<style>
* {
    box-sizing: border-box;
    margin: 0;
    padding: 0;
}

body {
    font-family: Arial, Helvetica, sans-serif;
    line-height: 1.4;
}

.btn {
    display: inline-block;
    border: none;
    background: #555;
    color: #fff;
    padding: 7px 20px;
    cursor: pointer;
}

.btn:hover {
    background: #666;
}
</style>
