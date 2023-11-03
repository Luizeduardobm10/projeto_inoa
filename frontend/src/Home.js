
import React from 'react';
import axios from 'axios'
import './Home.css';
import { Link } from "react-router-dom";

// function LoginLayout() {
  
//   let navigate = useNavigate(); 
//   const routeChange = () =>{ 
//     let path = 'novoativo'; 
//     navigate(path);
//   }
  
//   return (
//      <div className="app flex-row align-items-center">
//       <button onClick={routeChange}>Adicionar novo ativo</button>
//     </div>
//   );
// }

class Home extends React.Component {

  
  state ={ details: [], }
  
  componentDidMount() {

    let data;
    axios.get('http://localhost:8000')
      .then(res =>{
        data = res.data;
        this.setState({
          details: data
        });
      })
      .catch(err => {})
}

    render() {
      return (
        <div>
      <Link to='/novoativo' class="button"> Adicionar novo ativo</Link>
        <table class="header">
          <thead>
              <th class="elements">Símbolo</th>
              <th class="elements">Nome</th>
              <th class="elements">Preço Atual</th>
              <th class="elements">Intervalo de monitoramento</th>
              <th class="elements">Limite para compra</th>
              <th class="elements">Limite para venda</th>


          </thead>
        </table>
        {this.state.details.map((output, id) => (
          <div key={id}>
            <table class ="dataframe">
              <tr >
                <td class="elements">{output.symbol}</td>
                <td class="elements">{output.name}</td>
                <td class="price">{output.actual_price.toFixed(2)}</td>
                <td class="elements">{output.monitor} minutos</td>
                <td class="min">{output.min}</td>
                <td class="max">{output.max}</td>
              </tr>
            </table>
          </div>
        ))}

      </div>
      )
    }

}



export default Home













// function Home() {
//     return (
//       <div>
//         <h1>Selecionar Ativo</h1>
//         <div>
//           <label htmlFor="selectAsset">Selecione o Ativo:</label>
//           <select id="selectAsset">
//             <option value="A">A</option>
//             <option value="B">B</option>
//             <option value="C">C</option>
//           </select>
//         </div>

//         <div>
//           <label htmlFor="assetSymbol">Símbolo:</label>
//           <input type="text" id="assetSymbol" readOnly value="Símbolo do Ativo Aqui" />
//         </div>
//       </div>
//     );
//   }

// export default Home;
