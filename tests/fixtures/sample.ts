interface UserConfig {
    name: string;
    email: string;
    role: "admin" | "user";
}

class AuthService {
    private users: Map<string, UserConfig>;

    constructor() {
        this.users = new Map();
    }

    addUser(config: UserConfig): void {
        this.users.set(config.email, config);
    }

    getUser(email: string): UserConfig | undefined {
        return this.users.get(email);
    }
}

function createDefaultUser(name: string): UserConfig {
    return {
        name,
        email: `${name.toLowerCase()}@example.com`,
        role: "user",
    };
}

export { AuthService, createDefaultUser, UserConfig };
