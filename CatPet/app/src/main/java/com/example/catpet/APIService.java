package com.example.catpet;


import com.google.gson.JsonObject;

import java.util.List;

import retrofit2.Call;
import retrofit2.http.Body;
import retrofit2.http.GET;
import retrofit2.http.POST;

public interface APIService {

    @POST("login")
    Call<JsonObject> loginUsuario(@Body JsonObject body);

    @POST("registro")
    Call<Void> registerCliente(@Body Cliente cliente);

    @GET("productos")
    Call<List<Producto>> obtenerProductos();


}

