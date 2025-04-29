export interface User {
    id: number;
    username: string;
    email: string;
    groups: string[];
}

const API = 'http://localhost:8000/api/users/';
const token = () => localStorage.getItem('token');

export async function findUsers(): Promise<User[]> {
    const res = await fetch(API, {
        headers: {
            'Authorization': `Token ${token()}`,
            'Content-Type': 'application/json'
        }
    });
    if (!res.ok) throw new Error('Erreur chargement utilisateurs');
    return res.json();
}

export async function deleteUser(id: number): Promise<void> {
    const res = await fetch(`${API}${id}/`, {
        method: 'DELETE',
        headers: { 'Authorization': `Token ${token()}` }
    });
    if (!res.ok) throw new Error('Erreur suppression utilisateur');
}
