package com.example.catpet;

public class Producto {
    private int referencia;
    private String nombre;
    private String descripcion;
    private double precio;

    // Getters
    public int getReferencia() { return referencia; }
    public String getNombre() { return nombre; }
    public String getDescripcion() { return descripcion; }
    public double getPrecio() { return precio; }

    // (Opcional) Constructor si lo necesitas
    public Producto(int referencia, String nombre, String descripcion, double precio) {
        this.referencia = referencia;
        this.nombre = nombre;
        this.descripcion = descripcion;
        this.precio = precio;
    }
}
