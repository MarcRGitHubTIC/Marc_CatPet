package com.example.catpet;

public class StoreItem {
    private String nombre;
    private double precio;
    private int imagenResId;

    public StoreItem(String nombre, double precio, int imagenResId) {
        this.nombre = nombre;
        this.precio = precio;
        this.imagenResId = imagenResId;
    }

    public String getNombre() { return nombre; }
    public double getPrecio() { return precio; }
    public int getImagenResId() { return imagenResId; }
}
