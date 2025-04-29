

<script>
// I want a script to list the 3 pages of the app (Admin, PlaylistMaker, Analyst) and enable it only if the user is in the group "admin", "playlist_creator" or "analyst" (via an API call to get the user groups).
import { get_groups } from '../service/AuthService';

export default{
    name: 'Main',
    data() {
        return {
            groups: []
        }
    },
    async get_groups() {
        try {
            const response = await get_groups();
            this.groups = response.data.groups; // Assuming the API returns an object with a 'groups' property
        } catch (error) {
            console.error('Error fetching groups:', error);
        }
    }
}
</script>