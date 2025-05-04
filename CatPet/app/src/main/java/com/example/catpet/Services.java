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

public class Services extends BaseActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_services);

        RecyclerView recyclerView = findViewById(R.id.recycler_services);
        recyclerView.setLayoutManager(new LinearLayoutManager(this));

        List<ServiceItem> items = new ArrayList<>();
        items.add(new ServiceItem("Consulta veterinaria", "Revisión general de tu mascota", R.drawable.logo));
        items.add(new ServiceItem("Peluquería", "Corte y baño para perros y gatos", R.drawable.logo));
        items.add(new ServiceItem("Vacunación", "Vacunas obligatorias y opcionales", R.drawable.logo));

        ServiceAdapter adapter = new ServiceAdapter(items);
        recyclerView.setAdapter(adapter);


        Log.d("DEBUG", "Actividad Services creada");

        @SuppressLint({"MissingInflatedId", "LocalSuppress"}) BottomNavigationView bottomNav = findViewById(R.id.bottom_nav);
        bottomNav.setSelectedItemId(R.id.nav_services);
        bottomNav.setOnItemSelectedListener(item -> {
            int id = item.getItemId();
            Intent intent = null;

            if (id == R.id.nav_services) {
                Log.d("DEBUG", "Se seleccionó Servicios");
                return true;

            } else if (id == R.id.nav_home) {
                Log.d("DEBUG", "Se seleccionó Home");
                intent = new Intent(this, Home.class);

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
