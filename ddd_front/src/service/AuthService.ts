export async function login(username: String, password: String) {
    try {
        const response = await fetch('http://localhost:8000/api/auth/login/', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                username: username,
                password: password
            })
        })

        if (!response.ok) {
            throw new Error('Échec de la requête API')
        }

        const data = await response.json()
        localStorage.setItem('token', data['token'])
    } catch (error) {
        console.error('Erreur lors de l\'appel API:', error)
    }
}

export function logout() {

}
