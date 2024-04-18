import React from "react";
import { render } from "react-dom";

const App = () => {

    return (
        <div>
            <h1>From React Page</h1>
        </div>
    )
}

export default App;

const appDiv = document.getElementById("app");
render(<App />, appDiv)

