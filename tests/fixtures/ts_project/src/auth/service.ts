import { User, AdminUser } from "./models";

export class AuthService {
    private users: Map<string, User>;

    constructor() {
        this.users = new Map();
    }

    addUser(user: User): void {
        this.users.set(user.id, user);
    }

    getUser(id: string): User | undefined {
        return this.users.get(id);
    }

    isAdmin(user: User): boolean {
        return user instanceof AdminUser;
    }
}

export function createSession(user: User): string {
    return `session_${user.id}_${Date.now()}`;
}
