package com.example.catpet;

public class Cliente {
    private String fullName;
    private String correo;
    private String telefono;
    private String user;
    private String pwd;

    public Cliente(String fullName, String correo, String telefono, String user, String pwd) {
        this.fullName = fullName;
        this.correo = correo;
        this.telefono = telefono;
        this.user = user;
        this.pwd = pwd;
    }

}
