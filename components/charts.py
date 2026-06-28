def style_chart(fig, title):
    fig.update_layout(
        title={
            "text": title,
            "x": 0.02,
            "font": {"size": 22}
        },
        template="plotly_white",
        paper_bgcolor="white",
        plot_bgcolor="white",
        height=430,
        margin=dict(l=40, r=40, t=70, b=40),
        hovermode="x unified",
        font=dict(size=13),
        legend=dict(
            orientation="h",
            y=1.08,
            x=0
        )
    )

    fig.update_xaxes(showgrid=False)
    fig.update_yaxes(gridcolor="#E5E7EB")

    return fig