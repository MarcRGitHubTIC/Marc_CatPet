package com.example.catpet;

import android.annotation.SuppressLint;
import android.content.Intent;
import android.os.Bundle;
import android.util.Log;

import androidx.recyclerview.widget.LinearLayoutManager;
import androidx.recyclerview.widget.RecyclerView;

import com.google.android.material.bottomnavigation.BottomNavigationView;

import java.util.ArrayList;
import java.util.List;

public class Store extends BaseActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_store);

        RecyclerView recyclerView = findViewById(R.id.recycler_store);
        recyclerView.setLayoutManager(new LinearLayoutManager(this));

        List<StoreItem> productos = new ArrayList<>();
        productos.add(new StoreItem("Pienso gato", 5.99, R.drawable.logo));
        productos.add(new StoreItem("Juguete", 3.49, R.drawable.logo));

        StoreAdapter adapter = new StoreAdapter(productos);
        recyclerView.setAdapter(adapter);


        Log.d("DEBUG", "Actividad Store creada");

        @SuppressLint({"MissingInflatedId", "LocalSuppress"}) BottomNavigationView bottomNav = findViewById(R.id.bottom_nav);
        bottomNav.setSelectedItemId(R.id.nav_store);
        bottomNav.setOnItemSelectedListener(item -> {
            int id = item.getItemId();
            Intent intent = null;

            if (id == R.id.nav_store) {
                Log.d("DEBUG", "Se seleccionó Tienda");
                return true;

            } else if (id == R.id.nav_home) {
                Log.d("DEBUG", "Se seleccionó Home");
                intent = new Intent(this, Home.class);

            } else if (id == R.id.nav_services) {
                Log.d("DEBUG", "Se seleccionó Servicios");
                intent = new Intent(this, Services.class);

            } else if (id == R.id.nav_contacts) {
                Log.d("DEBUG", "Se seleccionó Contactos");
                intent = new Intent(this, Contactos.class);
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
