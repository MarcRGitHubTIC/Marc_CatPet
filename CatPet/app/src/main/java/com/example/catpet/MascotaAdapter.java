package com.example.catpet;

import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ImageView;
import android.widget.TextView;

import androidx.annotation.NonNull;
import androidx.recyclerview.widget.RecyclerView;

import java.util.List;

public class MascotaAdapter extends RecyclerView.Adapter<MascotaAdapter.MascotaViewHolder> {

    private final List<MascotaItem> lista;

    public MascotaAdapter(List<MascotaItem> lista) {
        this.lista = lista;
    }

    @NonNull
    @Override
    public MascotaViewHolder onCreateViewHolder(@NonNull ViewGroup parent, int viewType) {
        View vista = LayoutInflater.from(parent.getContext()).inflate(R.layout.item_mascota, parent, false);
        return new MascotaViewHolder(vista);
    }

    @Override
    public void onBindViewHolder(@NonNull MascotaViewHolder holder, int position) {
        MascotaItem item = lista.get(position);
        holder.titulo.setText(item.getTitulo());
        holder.descripcion.setText(item.getDescripcion());
        holder.imagen.setImageResource(item.getImagen());
    }

    @Override
    public int getItemCount() {
        return lista.size();
    }

    public static class MascotaViewHolder extends RecyclerView.ViewHolder {
        TextView titulo, descripcion;
        ImageView imagen;

        public MascotaViewHolder(@NonNull View itemView) {
            super(itemView);
            titulo = itemView.findViewById(R.id.titulo_mascota);
            descripcion = itemView.findViewById(R.id.descripcion_mascota);
            imagen = itemView.findViewById(R.id.imagen_mascota);
        }
    }
}
