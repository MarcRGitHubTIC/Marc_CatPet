package com.example.catpet;

import android.annotation.SuppressLint;
import android.content.Intent;
import android.os.Bundle;
import android.util.Log;

import com.google.android.material.bottomnavigation.BottomNavigationView;

public class Home extends BaseActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_home);

        Log.d("DEBUG", "Actividad Home creada");

        @SuppressLint({"MissingInflatedId", "LocalSuppress"}) BottomNavigationView bottomNav = findViewById(R.id.bottom_nav);
        bottomNav.setOnItemSelectedListener(item -> {
            int id = item.getItemId();
            Intent intent = null;

            if (id == R.id.nav_home) {
                Log.d("DEBUG", "Se seleccionó Home");
                return true;

            } else if (id == R.id.nav_services) {
                Log.d("DEBUG", "Se seleccionó Servicios");
                intent = new Intent(this, Services.class);

            } else if (id == R.id.nav_contacts) {
                Log.d("DEBUG", "Se seleccionó Contactos");
                intent = new Intent(this, Contactos.class);

            } else if (id == R.id.nav_store) {
                Log.d("DEBUG", "Se seleccionó Tienda");
                intent = new Intent(this, Store.class);
            }

            if (intent != null) {
                startActivity(intent);
                overridePendingTransition(0, 0);
                finish();
            } else {
                Log.e("ERROR", "Intent es NULL, no se pudo iniciar la actividad");
            }

            return true;
        });
    }
}
