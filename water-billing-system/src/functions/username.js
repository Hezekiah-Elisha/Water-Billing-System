import axios from 'axios';

export default function username(){
    const token = localStorage.getItem('token');
    const config = {
        headers: {
            Authorization: `Bearer ${token}`
        }
    };
    
    axios.get('http://localhost:7000/auth/users/username', config)
        .then(response => {
            let name = response.data["username"];
            // console.log(name);
            return `${name}`;
        }).catch(error => {
            return error
        });
}