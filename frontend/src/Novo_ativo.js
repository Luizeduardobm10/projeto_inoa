
import axios from 'axios';
import React from 'react';
import {useState} from 'react';

function NovoAtivo() {



const [symbol,setSymbol] = useState();


let postForm = function () {
  axios.post('http://localhost:8000/',{symbol})
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
          </select>
        </div>
        <p>{symbol}</p>
        <input type='submit' value='Save'></input>
      </form>
    </div>
  );
}

export default NovoAtivo;