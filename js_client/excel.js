const LoginExcel = document.getElementById("excel-form")
const classe = document.getElementById("classe")

const endpointBase = "http://belle-rose.localhost:8000/ecole/v1/eleve-create/"

if (LoginExcel) {
    LoginExcel.addEventListener('submit', (e) => {
        classe.value = "CP1"
        e.preventDefault();

        const loginFormData = new FormData(LoginExcel);

        const options = {
            method: "POST",
            body: loginFormData, // Ne pas utiliser JSON.stringify(), c'est un formulaire multipart
        };

        fetch(endpointBase, options)
            .then((response) => {
                console.log(response);
                return response.json();
            })
            .then((authData) => {
                console.log(authData);
            })
            .catch((err) => {
                console.log("erreur", err);
            });
    });
}
