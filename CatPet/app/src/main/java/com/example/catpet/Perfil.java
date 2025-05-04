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

public class Perfil extends BaseActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_perfil);

        RecyclerView recyclerView = findViewById(R.id.recycler_perfil);
        recyclerView.setLayoutManager(new LinearLayoutManager(this));

        List<HomeItem> items = new ArrayList<>();
        items.add(new HomeItem("Mis datos", "Consulta y modifica tu información", R.drawable.logo));
        items.add(new HomeItem("Mis mascotas", "Lista de tus mascotas registradas", R.drawable.logo));
        items.add(new HomeItem("Preferencias", "Gestiona tus configuraciones", R.drawable.logo));

        HomeAdapter adapter = new HomeAdapter(items);
        recyclerView.setAdapter(adapter);

        Log.d("DEBUG", "Actividad Perfil creada");

        @SuppressLint({"MissingInflatedId", "LocalSuppress"}) BottomNavigationView bottomNav = findViewById(R.id.bottom_nav);
        bottomNav.setOnItemSelectedListener(item -> {
            int id = item.getItemId();
            Intent intent = null;

            if (id == R.id.nav_home) {
                Log.d("DEBUG", "Se seleccionó Home");
                intent = new Intent(this, Home.class);

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
