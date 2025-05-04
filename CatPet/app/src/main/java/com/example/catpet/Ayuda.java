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

public class Ayuda extends BaseActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_ayuda);

        RecyclerView recyclerView = findViewById(R.id.recycler_ayuda);
        recyclerView.setLayoutManager(new LinearLayoutManager(this));

        List<AyudaItem> items = new ArrayList<>();
        items.add(new AyudaItem("¿Cómo registrar una mascota?", "Ve a la sección Perfil y pulsa en 'Añadir Mascota'.", R.drawable.logo));
        items.add(new AyudaItem("¿Cómo agendar una cita?", "En la sección Servicios puedes ver y reservar citas.", R.drawable.logo));
        items.add(new AyudaItem("¿Dónde consultar las vacunas?", "Ingresa en la sección Mascota y selecciona Vacunas.", R.drawable.logo));

        AyudaAdapter adapter = new AyudaAdapter(items);
        recyclerView.setAdapter(adapter);

        @SuppressLint("MissingInflatedId") BottomNavigationView bottomNav = findViewById(R.id.bottom_nav);
        bottomNav.setOnItemSelectedListener(item -> {
            Intent intent = null;
            int id = item.getItemId();

            if (id == R.id.nav_home) {
                intent = new Intent(this, Home.class);
            } else if (id == R.id.nav_services) {
                intent = new Intent(this, Services.class);
            } else if (id == R.id.nav_contacts) {
                intent = new Intent(this, Contactos.class);
            } else if (id == R.id.nav_store) {
                intent = new Intent(this, Store.class);
            }

            if (intent != null) {
                startActivity(intent);
                overridePendingTransition(0, 0);
                finish();
            }

            return true;
        });
    }
}
