export default {
    template: "<div></div>",
    mounted() {
        this.keycloak = globalKeycloakInstance;
    },
    methods: {
        initialize(initConfig) {
            this.keycloak.init(initConfig).then(
                    authenticated => {
                        if (authenticated) {
                            this.keycloak.onTokenExpired = this.keycloak.updateToken;
                        }
                    }

            );
        },
        getToken() {
            return this.keycloak.token;
        }
        ,
        isAuthenticated() {
            return this.keycloak.authenticated;
        }
    }
};