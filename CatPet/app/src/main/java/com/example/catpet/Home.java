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

public class Home extends BaseActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_home);

        RecyclerView recyclerView = findViewById(R.id.recycler_home);
        recyclerView.setLayoutManager(new LinearLayoutManager(this));

        List<HomeItem> items = new ArrayList<>();
        items.add(new HomeItem("Veterinaria", "Consulta tu historial médico y vacunas", R.drawable.logo));
        items.add(new HomeItem("Adopciones", "Conoce animales que buscan un hogar", R.drawable.logo));
        items.add(new HomeItem("Blog", "Lee consejos de expertos sobre mascotas", R.drawable.logo));

        HomeAdapter adapter = new HomeAdapter(items);
        recyclerView.setAdapter(adapter);


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
