package com.demo.ecom;


import java.util.List;
import java.util.Scanner;


public class Main {
    public static void main(String[] args) {
        List<Product> products = DataStore.sampleProducts();
        Cart cart = new Cart();
        Scanner sc = new Scanner(System.in);
        while (true) {
            System.out.println("\n1) List products 2) Add to cart 3) Show cart 4) Checkout 0) Exit");
            int cmd = sc.nextInt();
            if (cmd == 0) break;
            switch (cmd) {
                case 1:
                    products.forEach(System.out::println);
                    break;
                case 2:
                    System.out.print("Enter product id: ");
                    int id = sc.nextInt();
                    products.stream().filter(p -> p.getId() == id).findFirst().ifPresent(cart::add);
                    break;
                case 3:
                    cart.show();
                    break;
                case 4:
                    System.out.println("Total: ₹" + cart.total());
                    System.out.println("Thank you for shopping!");
                    return;
            }
        }
    }
}
