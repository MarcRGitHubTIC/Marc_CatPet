package com.example.catpet;

public class ContactItem {
    private String nombre;
    private String info;
    private int imagenResId;

    public ContactItem(String nombre, String info, int imagenResId) {
        this.nombre = nombre;
        this.info = info;
        this.imagenResId = imagenResId;
    }

    public String getNombre() { return nombre; }
    public String getInfo() { return info; }
    public int getImagenResId() { return imagenResId; }
}
