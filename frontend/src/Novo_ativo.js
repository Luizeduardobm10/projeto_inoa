
import axios from 'axios';
import React from 'react';
import {useState} from 'react';

function NovoAtivo() {



const [symbol,setSymbol] = useState();
const [monitor,setMonitor] = useState();
const [min,setMin] = useState();
const [max,setMax] = useState();



let postForm = function () {
  axios.post('http://localhost:8000/',{symbol,monitor,min,max})
    .then(res => console.log(res))
    .catch(err => console.log(err))
}


  return (
    <div>
      <form onSubmit={postForm}>
        <div>
        <label htmlFor="selectAsset" >Selecione o Ativo:</label>
          <select id="selectAsset" onChange={(e) => setSymbol(e.target.value)}>
            <option value="BPAC5.SA">BPAC5.SA</option>
            <option value="PETR4.SA">PETR4.SA</option>
            <option value="RADL3.SA">RADL3.SA</option>
            <option value="TIMP3.SA">TIMP3.SA</option>
            <option value="JBSS3.SA">JBSS3.SA</option>
            <option value="ECOR3.SA">ECOR3.SA</option>
            <option value="UGPA3.SA">UGPA3.SA</option>
            <option value="ITSA4.SA">ITSA4.SA</option>
            <option value="CCRO3.SA">CCRO3.SA</option>
            <option value="OIBR4.SA">OIBR4.SA</option>

          </select>
        </div>
        <div>
        <label htmlFor="selectAsset" >Periodicidade do monitoramento:</label>
          <select id="selectAsset" onChange={(e) => setMonitor(e.target.value)}>
            <option value="1">1</option>
            <option value="5">5</option>
            <option value="10">10</option>
          </select>
        </div>
        <label>Valor para compra:
        <input type='text' onChange={(e) => setMin(e.target.value)}></input>
        </label>
        <label>Valor para venda:
        <input type='text' onChange={(e) => setMax(e.target.value)}></input>
        </label>
        <input type='submit' value='Save'></input>
      </form>
    </div>
  );
}

export default NovoAtivo;