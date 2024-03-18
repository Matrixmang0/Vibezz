const profile = {
  template: `
  <div>
    <h1>Profile</h1>
    <p>Name: {{profile.name}}</p>
    <p>Username: {{profile.username}}</p>
    <p>Email: {{profile.email}}</p>
    <p>Role: {{profile.role_id}}</p>
  </div>`,

  data() {
    return {
      profile: {
        id: 0,
        name: "Santhosh",
        username: "santhosh",
        email: "XXXXXXXXXXXXXXXXXX",
        role_id: "usr"
      },

      success: true,
      error: "Error",
    }
  },

  async mounted() {
    const response = await fetch('/api/user/0');
    if (response.ok){
      const data = await response.json();
      this.profile = data;
    }
    else{
      console.log("Error");
    }
    this.profile = response.data;
  },
}

export default profile;