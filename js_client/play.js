const decode = (token) =>
  decodeURIComponent(
    atob(token.split(".")[1].replace("-", "+").replace("_", "/"))
      .split("")
      .map((c) => `%${("00" + c.charCodeAt(0).toString(16)).slice(-2)}`)
      .join("")
  );


const LoginForm = document.getElementById("login-form");

const baseEndpoint = "http://localhost:8000/api";
const salle = document.getElementById("salle");
const endpointProf = "http://belle-rose.localhost:8000/professeur/v2/professeur";
const endpointBase = "http://belle-rose.localhost:8000/eleve/v2/eleve/";

if (LoginForm) {
  LoginForm.addEventListener("submit", (e) => {
    e.preventDefault();
    const loginEndpoint = `${baseEndpoint}/token/`;

    const loginFormData = new FormData(LoginForm);

    const loginObjectData = Object.fromEntries(loginFormData);

    const bodyJsonData = JSON.stringify(loginObjectData);

    const options = {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: bodyJsonData,
    };
    fetch(loginEndpoint, options)
      .then((response) => {
        console.log(response);
        return response.json();
      })
      .then((authData) => {
        console.log(authData);
        localStorage.setItem("access", authData.access);
        localStorage.setItem("refresh", authData.refresh);
        handleAuthData(authData, getEleve());
      })
      .catch((err) => {
        console.log("erreur", err);
      });
  });
}

function handleAuthData(authData, callback) {
  localStorage.setItem("access", authData.access);
  localStorage.setItem("refresh", authData.refresh);
  if (callback) {
    callback();
  }
};

function wrtiteTocontainer(data) {
  if (salle) {
    salle.innerHTML = `<p> Voici la liste de salle disponible pour cette école \n ${JSON.stringify(
      data
    )}</p>`;
  }
}

function getSalle() {
    code_token = localStorage.getItem("access")
    const decodedToken = decode(`
        ${code_token}
    `);
    const code_json = JSON.parse(decodedToken)
    console.log(code_json);
    console.log(code_json.schema_name);
    let endpoint
    if (code_json.schema_name != null){
       endpoint = `http://${code_json.schema_name.replace("_", "-")}.localhost:8000/ecole/salle/1/`;
    }
    else{
       endpoint = "http://localhost:8000/inscription/ecole"
    }
  const options = {
    method: "GET",
    headers: {
      "Content-Type": "application/json",
      "Authorization": `Bearer ${code_token}`,
    },
  };
  fetch(endpoint, options)
    .then((response) => response.json())
    .then((data) => {
      wrtiteTocontainer(data);
    });
}

function getEleve() {

  const options = {
    method: 'GET',
    headers: {
      "Content-Type": "application/json",
      "niveau": "CP1"
    },
  };
  fetch(endpointBase, options)
    .then((response) => {
      console.log(response);
      return response.json();
    }) 
    
    .then((data) => {
      wrtiteTocontainer(data)
      console.log(data);
    });
}