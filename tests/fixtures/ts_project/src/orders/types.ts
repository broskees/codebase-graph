import { User } from "../auth/models";

export interface OrderItem {
    productId: string;
    quantity: number;
    price: number;
}

export class Order {
    id: string;
    user: User;
    items: OrderItem[];
    total: number;

    constructor(id: string, user: User, items: OrderItem[]) {
        this.id = id;
        this.user = user;
        this.items = items;
        this.total = items.reduce((sum, item) => sum + item.price * item.quantity, 0);
    }
}

export function calculateTotal(items: OrderItem[]): number {
    return items.reduce((sum, item) => sum + item.price * item.quantity, 0);
}
