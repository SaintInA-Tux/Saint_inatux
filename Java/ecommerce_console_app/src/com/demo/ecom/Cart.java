package com.demo.ecom;


import java.util.ArrayList;
import java.util.List;


public class Cart {
    private final List<Product> items = new ArrayList<>();


    public void add(Product p) { items.add(p); }
    public void remove(Product p) { items.remove(p); }
    public double total() {
        return items.stream().mapToDouble(Product::getPrice).sum();
    }
    public void show() {
        if (items.isEmpty()) System.out.println("Cart is empty");
        else items.forEach(System.out::println);
    }
}
