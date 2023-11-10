
import axios from 'axios';
import React from 'react';
import {useState} from 'react';
import './Novoativo.css';
import {useNavigate} from 'react-router-dom';

function NovoAtivo() {


const history = useNavigate();
const [symbol,setSymbol] = useState();
const [monitor,setMonitor] = useState();
const [min,setMin] = useState();
const [max,setMax] = useState();



let postForm = function () {
  axios.post('http://localhost:8000/',{symbol,monitor,min,max})
    .then(res => console.log(res))
    .catch(err => console.log(err))
  history('/');
}


  return (
    <div class="container">
      <form  onSubmit={postForm}>
        <div class="label1">
        <label  htmlFor="selectAsset" >Selecione o Ativo:</label>
          <select class="select1" id="selectAsset" onChange={(e) => setSymbol(e.target.value)}>
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
        <div class="label2">
          <br></br>
        <label class="" htmlFor="selectAsset" >Periodicidade do monitoramento(minutos):</label>
          <select class="select2"id="selectAsset" onChange={(e) => setMonitor(e.target.value)}>
            <option value="1">1</option>
            <option value="5">5</option>
            <option value="10">10</option>
            <option value="30">30</option>
            <option value="60">60</option>
          </select>
        </div>
        <br></br>
        <div class="label3">
          <label >Valor para compra:
            <input class="input2" type='text'  onChange={(e) => setMin(e.target.value)}></input>
          </label>
        </div>
        <br></br>
        <div class="label4">
          <label >Valor para venda:
            <input class="input2" type='text' onChange={(e) => setMax(e.target.value)}></input>
          </label>
        </div>
        <br></br>
        <div class="button1">
          <input  type='submit' value='Save'></input>
        </div>
      </form>
    </div>

  );
}

export default NovoAtivo;