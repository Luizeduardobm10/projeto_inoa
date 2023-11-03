
import Home from "./Home.js";
import NovoAtivo from "./Novo_ativo.js";
import { BrowserRouter, Routes, Route} from "react-router-dom";
import React from 'react'


function App() {
  return (
    <BrowserRouter>
      <Routes>
        <Route exact path="/" element={<Home />} />
        <Route path="novoativo/" element={<NovoAtivo />} />
      </Routes>
    </BrowserRouter>
  );
}
export default App;