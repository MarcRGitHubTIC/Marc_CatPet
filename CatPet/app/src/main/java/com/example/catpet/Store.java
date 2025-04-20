package com.example.catpet;

import android.content.Intent;
import android.os.Bundle;
import android.util.Log;
import android.view.MenuItem;
import androidx.activity.EdgeToEdge;
import androidx.annotation.NonNull;
import androidx.appcompat.app.AppCompatActivity;
import com.google.android.material.bottomnavigation.BottomNavigationView;

public class Store extends AppCompatActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        EdgeToEdge.enable(this);
        setContentView(R.layout.activity_store);
        Log.d("DEBUG", "Actividad Store creada");

        BottomNavigationView bottomNavigationView = findViewById(R.id.bottom_navigation);

        bottomNavigationView.setSelectedItemId(R.id.nav_store);

        bottomNavigationView.setOnItemSelectedListener(new BottomNavigationView.OnItemSelectedListener() {
            @Override
            public boolean onNavigationItemSelected(@NonNull MenuItem item) {
                Log.d("DEBUG", "Elemento del menú seleccionado: " + item.getTitle());

                Intent intent = null;
                int itemId = item.getItemId();

                if (itemId == R.id.nav_store) {
                    Log.d("DEBUG", "Se seleccionó Tienda");
                    return true;
                }

                if (itemId == R.id.nav_home) {
                    Log.d("DEBUG", "Se seleccionó Home");
                    intent = new Intent(Store.this, Home.class);
                } else if (itemId == R.id.nav_services) {
                    Log.d("DEBUG", "Se seleccionó Servicios");
                    intent = new Intent(Store.this, Services.class);
                } else if (itemId == R.id.nav_contacts) {
                    Log.d("DEBUG", "Se seleccionó Contactos");
                    intent = new Intent(Store.this, Contactos.class);
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
