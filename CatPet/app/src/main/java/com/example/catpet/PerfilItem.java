package com.example.catpet;

public class PerfilItem {
    private String texto;
    private int iconoResId;

    public PerfilItem(String texto, int iconoResId) {
        this.texto = texto;
        this.iconoResId = iconoResId;
    }

    public String getTexto() { return texto; }
    public int getIconoResId() { return iconoResId; }
}
