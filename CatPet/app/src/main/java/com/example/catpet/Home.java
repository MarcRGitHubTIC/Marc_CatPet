package com.example.catpet;

import android.util.Log;
import android.content.Intent;
import android.os.Bundle;
import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;
import com.google.android.material.bottomnavigation.BottomNavigationView;
import com.google.android.material.navigation.NavigationBarView;

import android.view.MenuItem;

public class Home extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_home);
        Log.d("DEBUG", "Actividad Home creada");

        BottomNavigationView bottomNavigationView = findViewById(R.id.bottom_navigation);

        bottomNavigationView.setOnItemSelectedListener(new NavigationBarView.OnItemSelectedListener() {
            @Override
            public boolean onNavigationItemSelected(@NonNull MenuItem item) {
                Log.d("DEBUG", "Elemento del menú seleccionado: " + item.getTitle());

                Intent intent = null;
                if (item.getItemId() == R.id.nav_home) {
                    Log.d("DEBUG", "Se seleccionó Home");
                    return true;
                } else if (item.getItemId() == R.id.nav_services) {
                    Log.d("DEBUG", "Se seleccionó Servicios");
                    intent = new Intent(Home.this, Services.class);
                } else if (item.getItemId() == R.id.nav_contacts) {
                    Log.d("DEBUG", "Se seleccionó Contactos");
                    intent = new Intent(Home.this, Contactos.class);
                } else if (item.getItemId() == R.id.nav_store) {
                    Log.d("DEBUG", "Se seleccionó Tienda");
                    intent = new Intent(Home.this, Store.class);
                }

                if (intent != null) {
                    Log.d("DEBUG", "Iniciando nueva actividad: " + intent.getComponent());
                    startActivity(intent);
                    overridePendingTransition(0, 0);
                    finish();
                } else {
                    Log.e("ERROR", "Intent es NULL, no se pudo iniciar la actividad");
                }

                return true;
            }
        });
    }
}