package com.example.catpet;

import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ImageView;
import android.widget.TextView;

import androidx.annotation.NonNull;
import androidx.recyclerview.widget.RecyclerView;

import java.util.List;

public class StoreAdapter extends RecyclerView.Adapter<StoreAdapter.StoreViewHolder> {

    private List<StoreItem> productos;

    public StoreAdapter(List<StoreItem> productos) {
        this.productos = productos;
    }

    @NonNull
    @Override
    public StoreViewHolder onCreateViewHolder(@NonNull ViewGroup parent, int viewType) {
        View view = LayoutInflater.from(parent.getContext()).inflate(R.layout.item_store, parent, false);
        return new StoreViewHolder(view);
    }

    @Override
    public void onBindViewHolder(@NonNull StoreViewHolder holder, int position) {
        StoreItem producto = productos.get(position);
        holder.nombre.setText(producto.getNombre());
        holder.precio.setText(String.format("%.2f€", producto.getPrecio()));
        holder.imagen.setImageResource(R.drawable.logo);
    }

    @Override
    public int getItemCount() {
        return productos.size();
    }

    static class StoreViewHolder extends RecyclerView.ViewHolder {
        TextView nombre, precio;
        ImageView imagen;

        public StoreViewHolder(@NonNull View itemView) {
            super(itemView);
            nombre = itemView.findViewById(R.id.txt_product_name);
            precio = itemView.findViewById(R.id.txt_product_price);
            imagen = itemView.findViewById(R.id.img_product);
        }
    }
}

