const defaultUrl = "http://localhost:8000/api/songs";

export async function generatePlaylist(countrySource: string, songSource: string, countryCible: string) {
    let token = localStorage.getItem('token');
    try {
        const apiResponse = await fetch(`${defaultUrl}/generate-playlist`, {
            method: 'POST',
            headers: {
                'Authorization': `Token ${token}`,
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                country_source: countrySource,
                music: songSource,
                country_cible: countryCible,
            })
        });
        if (!apiResponse.ok) {
            throw new Error('Failed to find groups');
        }
        let response = await apiResponse.json();
        return response;
    } catch (error) {
        console.log('Error during getting groups:', error);
        return [];
    }
}