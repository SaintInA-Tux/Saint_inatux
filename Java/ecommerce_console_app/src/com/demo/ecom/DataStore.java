package com.demo.ecom;


import java.util.ArrayList;
import java.util.List;


public class DataStore {
    public static List<Product> sampleProducts() {
        List<Product> p = new ArrayList<>();
        p.add(new Product(1, "Wireless Mouse", 499.0));
        p.add(new Product(2, "Mechanical Keyboard", 1999.0));
        p.add(new Product(3, "16GB USB Drive", 299.0));
        return p;
    }
}
