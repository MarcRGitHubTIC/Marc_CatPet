package com.example.catpet;

import android.content.Intent;
import android.os.Bundle;
import android.util.Log;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

import androidx.activity.EdgeToEdge;
import androidx.appcompat.app.AppCompatActivity;

import com.google.gson.JsonObject;

import retrofit2.Call;
import retrofit2.Callback;
import retrofit2.Response;

public class Login extends AppCompatActivity {

    private EditText usernameField;
    private EditText passwordField;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        EdgeToEdge.enable(this);
        setContentView(R.layout.activity_login);

        usernameField = findViewById(R.id.usernameField);
        passwordField = findViewById(R.id.passwordField);
        Button loginButton = findViewById(R.id.loginButton);
        Button registerButton = findViewById(R.id.registerButton);

        registerButton.setOnClickListener(v -> {
            Intent intent = new Intent(Login.this, Registro.class);
            startActivity(intent);
        });

        loginButton.setOnClickListener(v -> realizarLogin());
    }

    private void realizarLogin() {
        String correo = usernameField.getText().toString().trim();
        String password = passwordField.getText().toString().trim();

        if (correo.isEmpty() || password.isEmpty()) {
            Toast.makeText(this, "Por favor, completa todos los campos", Toast.LENGTH_SHORT).show();
            return;
        }

        JsonObject json = new JsonObject();
        json.addProperty("correo", correo);
        json.addProperty("pwd", password);

        APIService apiService = RetrofitClient.getClient().create(APIService.class);
        Call<JsonObject> call = apiService.loginUsuario(json);

        call.enqueue(new Callback<JsonObject>() {
            @Override
            public void onResponse(Call<JsonObject> call, Response<JsonObject> response) {
                if (response.isSuccessful() && response.body() != null) {
                    JsonObject body = response.body();
                    int status = body.get("status").getAsInt();

                    if (status == 1) {
                        Toast.makeText(Login.this, "Login exitoso", Toast.LENGTH_SHORT).show();
                        startActivity(new Intent(Login.this, Home.class));
                        finish();
                    } else {
                        Toast.makeText(Login.this, body.get("message").getAsString(), Toast.LENGTH_SHORT).show();
                        Log.d("LOGIN_RESPONSE", body.get("message").getAsString());
                    }
                } else {
                    Toast.makeText(Login.this, "Error en la respuesta del servidor", Toast.LENGTH_SHORT).show();
                }
            }

            @Override
            public void onFailure(Call<JsonObject> call, Throwable t) {
                Toast.makeText(Login.this, "Error de red: " + t.getMessage(), Toast.LENGTH_LONG).show();
                Log.d("LOGIN_RESPONSE", "Error de red: " + t.getMessage());
            }

        });
    }
}
