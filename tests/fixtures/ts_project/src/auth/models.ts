export interface Authenticatable {
    id: string;
    authenticate(token: string): boolean;
}

export interface Serializable {
    toJSON(): string;
}

export class User implements Authenticatable, Serializable {
    id: string;
    name: string;
    email: string;

    constructor(id: string, name: string, email: string) {
        this.id = id;
        this.name = name;
        this.email = email;
    }

    authenticate(token: string): boolean {
        return token.length > 0;
    }

    toJSON(): string {
        return JSON.stringify({ id: this.id, name: this.name });
    }
}

export class AdminUser extends User {
    permissions: string[];

    constructor(id: string, name: string, email: string, permissions: string[]) {
        super(id, name, email);
        this.permissions = permissions;
    }
}
