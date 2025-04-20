package com.example.catpet;


import retrofit2.Call;
import retrofit2.http.Body;
import retrofit2.http.GET;
import retrofit2.http.POST;

public interface APIService {
    @POST("registro")
    Call<Void> registerCliente(@Body Cliente cliente);

}

