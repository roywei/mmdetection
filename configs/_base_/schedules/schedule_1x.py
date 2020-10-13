# optimizer
optimizer = dict(type='SGD', lr=0.24, momentum=0.9, weight_decay=0.0001)
optimizer_config = dict(grad_clip=None)
# learning policy
lr_config = dict(
    policy='step',
    warmup='linear',
    warmup_iters=1800,
    warmup_ratio=0.000133,
    step=[12, 16])
total_epochs = 25
