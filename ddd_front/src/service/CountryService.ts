const defaultUrl = "http://localhost:8000/api/countries";

export async function findCountries() {
    let token = localStorage.getItem('token');
    try {
        const response = await fetch(`${defaultUrl}/`, {
            method: 'GET',
            headers: {
                'Authorization': `Token ${token}`,
                'Content-Type': 'application/json',
            }
        });
        if (!response.ok) {
            throw new Error('Failed to find groups');
        }
        let countries = (await response.json())['countries'];
        return countries;
    } catch (error) {
        console.log('Error during getting groups:', error);
    }
}

export async function findSongsByCountry(country: string) {
    let token = localStorage.getItem('token');
    try {
        const response = await fetch(`${defaultUrl}/${country}/songs`, {
            method: 'GET',
            headers: {
                'Authorization': `Token ${token}`,
                'Content-Type': 'application/json',
            }
        });
        if (!response.ok) {
            throw new Error('Failed to find groups');
        }
        return (await response.json())['songs'];
    } catch (error) {
        console.log('Error during getting groups:', error);
        return [];
    }
}