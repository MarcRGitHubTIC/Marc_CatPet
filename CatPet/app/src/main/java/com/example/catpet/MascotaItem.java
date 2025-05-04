package com.example.catpet;

public class MascotaItem {
    private String titulo;
    private String descripcion;
    private int imagen;

    public MascotaItem(String titulo, String descripcion, int imagen) {
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
