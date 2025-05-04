package com.example.catpet;

public class AyudaItem {
    private final String titulo;
    private final String descripcion;
    private final int imagen;

    public AyudaItem(String titulo, String descripcion, int imagen) {
        this.titulo = titulo;
        this.descripcion = descripcion;
        this.imagen = imagen;
    }

    public String getTitulo() {
        return titulo;
    }

    public String getDescripcion() {
        return descripcion;
    }

    public int getImagen() {
        return imagen;
    }
}
