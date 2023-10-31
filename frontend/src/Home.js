
import { useNavigate } from "react-router-dom";
import React from 'react';
import axios from 'axios'
import { browserHistory, Router, Route } from 'react-router';

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
        {this.state.details.map((output,id) => (
          <div key={id}>
            <div>
              <h2>{output.symbol}</h2>
              <h2>{output.name}</h2>
              <h2>{output.date}</h2>
              <h2>{output.price}</h2>
            </div>
          </div>
        ))}
        <button href='/novoativo'>Adicionar novo ativo</button>
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
