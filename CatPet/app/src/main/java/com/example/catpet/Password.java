package com.example.catpet;

import android.os.Bundle;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

import androidx.activity.EdgeToEdge;
import androidx.appcompat.app.AppCompatActivity;
import androidx.core.graphics.Insets;
import androidx.core.view.ViewCompat;
import androidx.core.view.WindowInsetsCompat;

public class Password extends AppCompatActivity {

    private EditText emailEditText;
    private EditText confirmEmailEditText;
    private Button confirmButton;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        EdgeToEdge.enable(this);
        setContentView(R.layout.activity_password);
        emailEditText = findViewById(R.id.emailEditText);
        confirmEmailEditText = findViewById(R.id.confirmEmailEditText);
        confirmButton = findViewById(R.id.confirmButton);

        confirmButton.setOnClickListener(view -> {
            String email = emailEditText.getText().toString();
            String confirmEmail = confirmEmailEditText.getText().toString();

            if (email.equals(confirmEmail)) {
                // Pendiente
                Toast.makeText(Password.this, "Correo confirmado", Toast.LENGTH_SHORT).show();
            } else {
                Toast.makeText(Password.this, "Los correos no coinciden", Toast.LENGTH_SHORT).show();
            }
        });
    }
}