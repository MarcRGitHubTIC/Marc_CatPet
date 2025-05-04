package com.example.catpet;

import android.view.LayoutInflater;
import android.view.View;
import android.view.ViewGroup;
import android.widget.ImageView;
import android.widget.TextView;

import androidx.annotation.NonNull;
import androidx.recyclerview.widget.RecyclerView;

import java.util.List;

public class HomeAdapter extends RecyclerView.Adapter<HomeAdapter.HomeViewHolder> {

    private List<HomeItem> items;

    public HomeAdapter(List<HomeItem> items) {
        this.items = items;
    }

    @NonNull
    @Override
    public HomeViewHolder onCreateViewHolder(@NonNull ViewGroup parent, int viewType) {
        View view = LayoutInflater.from(parent.getContext()).inflate(R.layout.item_home, parent, false);
        return new HomeViewHolder(view);
    }

    @Override
    public void onBindViewHolder(@NonNull HomeViewHolder holder, int position) {
        HomeItem item = items.get(position);
        holder.titulo.setText(item.getTitulo());
        holder.descripcion.setText(item.getDescripcion());
        holder.imagen.setImageResource(item.getImagenResId());
    }

    @Override
    public int getItemCount() {
        return items.size();
    }

    static class HomeViewHolder extends RecyclerView.ViewHolder {
        TextView titulo, descripcion;
        ImageView imagen;

        public HomeViewHolder(@NonNull View itemView) {
            super(itemView);
            titulo = itemView.findViewById(R.id.txt_title);
            descripcion = itemView.findViewById(R.id.txt_description);
            imagen = itemView.findViewById(R.id.img_home);
        }
    }
}
