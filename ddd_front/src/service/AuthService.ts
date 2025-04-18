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
        return true;
    } catch (error) {
        console.error('Erreur lors de l\'appel API:', error)
        return false;
    }
}

export async function logout() {
    let token = localStorage.getItem('token');
    if (!token) {
        console.log("No token found, cannot log out.");
        return;
    }

    localStorage.clear();

    try {
        console.log('Token : ' + token);

        const response = await fetch('http://localhost:8000/api/auth/logout/', {
            method: 'DELETE',
            headers: {
                'Authorization': `Token ${token}`,
                'Content-Type': 'application/json',
            }
        });

        if (!response.ok) {
            throw new Error('Failed to log out');
        }

        console.log('Logout success:', await response.json());
    } catch (error) {
        console.log('Error during logout:', error);
    }
}

export async function getUserGroups() {
    let token = localStorage.getItem('token');
    try {
        const response = await fetch('http://localhost:8000/api/auth/groups', {
            method: 'GET',
            headers: {
                'Authorization': `Token ${token}`,
                'Content-Type': 'application/json',
            }
        });
        if (!response.ok) {
            throw new Error('Failed to find groups');
        }
        return (await response.json())['groups'];
    } catch (error) {
        console.log('Error during getting groups:', error);
    }
}
