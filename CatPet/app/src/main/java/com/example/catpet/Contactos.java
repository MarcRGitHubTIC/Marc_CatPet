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

public class Contactos extends BaseActivity {

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_contactos);

        RecyclerView recyclerView = findViewById(R.id.recycler_contacts);
        recyclerView.setLayoutManager(new LinearLayoutManager(this));

        List<ContactItem> contactList = new ArrayList<>();
        contactList.add(new ContactItem("Veterinario Principal", "veterinario@catpet.com", R.drawable.logo));
        contactList.add(new ContactItem("Soporte", "soporte@catpet.com", R.drawable.logo));
        contactList.add(new ContactItem("Atención al cliente", "+34 600 123 456", R.drawable.logo));

        ContactAdapter adapter = new ContactAdapter(contactList);
        recyclerView.setAdapter(adapter);


        Log.d("DEBUG", "Actividad Contactos creada");

        @SuppressLint({"MissingInflatedId", "LocalSuppress"}) BottomNavigationView bottomNav = findViewById(R.id.bottom_nav);
        bottomNav.setSelectedItemId(R.id.nav_contacts);

        bottomNav.setOnItemSelectedListener(item -> {
            int id = item.getItemId();
            Intent intent = null;

            if (id == R.id.nav_contacts) {
                Log.d("DEBUG", "Se seleccionó Contactos");
                return true;

            } else if (id == R.id.nav_home) {
                Log.d("DEBUG", "Se seleccionó Home");
                intent = new Intent(this, Home.class);

            } else if (id == R.id.nav_services) {
                Log.d("DEBUG", "Se seleccionó Servicios");
                intent = new Intent(this, Services.class);

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
