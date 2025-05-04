package com.example.catpet;

import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ImageView;
import android.widget.TextView;

import androidx.annotation.NonNull;
import androidx.recyclerview.widget.RecyclerView;

import java.util.List;

public class AyudaAdapter extends RecyclerView.Adapter<AyudaAdapter.ViewHolder> {

    private final List<AyudaItem> items;

    public AyudaAdapter(List<AyudaItem> items) {
        this.items = items;
    }

    @NonNull
    @Override
    public ViewHolder onCreateViewHolder(@NonNull ViewGroup parent, int viewType) {
        View vista = LayoutInflater.from(parent.getContext()).inflate(R.layout.item_ayuda, parent, false);
        return new ViewHolder(vista);
    }

    @Override
    public void onBindViewHolder(@NonNull ViewHolder holder, int position) {
        AyudaItem item = items.get(position);
        holder.titulo.setText(item.getTitulo());
        holder.descripcion.setText(item.getDescripcion());
        holder.imagen.setImageResource(item.getImagen());
    }

    @Override
    public int getItemCount() {
        return items.size();
    }

    static class ViewHolder extends RecyclerView.ViewHolder {
        TextView titulo, descripcion;
        ImageView imagen;

        public ViewHolder(@NonNull View itemView) {
            super(itemView);
            titulo = itemView.findViewById(R.id.titulo_ayuda);
            descripcion = itemView.findViewById(R.id.descripcion_ayuda);
            imagen = itemView.findViewById(R.id.imagen_ayuda);
        }
    }
}
